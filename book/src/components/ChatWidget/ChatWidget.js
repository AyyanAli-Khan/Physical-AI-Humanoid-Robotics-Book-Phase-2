import React, { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";
import "./ChatWidget.css";
import Link from "@docusaurus/Link";

const ChatWidget = () => {
  const fixDocPaths = (content) => {
    if (typeof content !== "string") return "";

    return (
      content
        // 1. Remove qdrant.com domain (with or without protocol)
        .replace(/https?:\/\/(www\.)?qdrant\.com/g, "")

        // 2. Ensure /physical-ai exists after /docs
        .replace(/\/docs\/(?!physical-ai\/)/g, "/docs/physical-ai/")

        // 3. Remove .mdx extension
        .replace(/\.mdx\b/g, "")
    );
  };

  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId, setSessionId] = useState(null);
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    const userMessage = {
      role: "user",
      content: inputValue,
      timestamp: new Date(),
    };
    const newMessages = [...messages, userMessage];
    setMessages(newMessages);
    setInputValue("");
    setIsLoading(true);

    try {
      // Call your backend API
      const response = await fetch(
        `${API_CONFIG.BASE_URL}${API_CONFIG.CHAT_ENDPOINT}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            message: inputValue,
            session_id: sessionId || undefined,
            model: API_CONFIG.DEFAULT_MODEL,
          }),
        }
      );

      const data = await response.json();

      if (response.ok) {
        if (data.session_id && !sessionId) {
          setSessionId(data.session_id);
        }

        const assistantMessage = {
          role: "assistant",
          content: data.response,
          sources: data.sources || [],
          timestamp: new Date(),
        };

        setMessages((prev) => [...prev, assistantMessage]);
      } else {
        const errorMessage = {
          role: "assistant",
          content: `Error: ${
            data.detail || "Failed to get response from the chatbot"
          }`,
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, errorMessage]);
      }
    } catch (error) {
      const errorMessage = {
        role: "assistant",
        content: `Error: ${
          error.message || "Failed to connect to the chatbot"
        }`,
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const toggleChat = () => {
    setIsOpen(!isOpen);
    if (!isOpen && inputRef.current) {
      setTimeout(() => inputRef.current?.focus(), 100);
    }
  };

  return (
    <div className="chat-widget">
      {isOpen ? (
        <div className="chat-container">
          <div className="chat-header">
            <h3>Documentation Assistant</h3>
            <button className="chat-close-btn" onClick={toggleChat}>
              ×
            </button>
          </div>

          <div className="chat-messages">
            {messages.length === 0 ? (
              <div className="chat-welcome">
                <p>
                  Hello! I'm your documentation assistant. Ask me anything about
                  the Physical AI & Humanoid Robotics content.
                </p>
              </div>
            ) : (
              messages.map((msg, index) => (
                <div
                  key={index}
                  className={`chat-message ${
                    msg.role === "user" ? "user-message" : "assistant-message"
                  }`}
                >
                  <div className="message-content">
                    {msg.role === "assistant" ? (
                      <ReactMarkdown
                        remarkPlugins={[remarkGfm]}
                        rehypePlugins={[rehypeRaw]}
                        components={{
                          // Custom components to handle various markdown elements
                          p: ({ node, ...props }) => <p {...props} />,
                          code: ({
                            node,
                            inline,
                            className,
                            children,
                            ...props
                          }) => {
                            const match = /language-(\w+)/.exec(
                              className || ""
                            );
                            return !inline && match ? (
                              <pre className={className}>
                                <code {...props} className={className}>
                                  {children}
                                </code>
                              </pre>
                            ) : (
                              <code className={className} {...props}>
                                {children}
                              </code>
                            );
                          },
                          a: ({ href = "", children }) => {
                            const isInternal = href.startsWith("/");

                            if (isInternal) {
                              return <Link to={href}>{children}</Link>;
                            }

                            return (
                              <a
                                href={href}
                                target="_blank"
                                rel="noopener noreferrer"
                              >
                                {children}
                              </a>
                            );
                          },
                          li: ({ node, ...props }) => <li {...props} />,
                          ul: ({ node, ...props }) => <ul {...props} />,
                          ol: ({ node, ...props }) => <ol {...props} />,
                          h1: ({ node, ...props }) => <h1 {...props} />,
                          h2: ({ node, ...props }) => <h2 {...props} />,
                          h3: ({ node, ...props }) => <h3 {...props} />,
                          h4: ({ node, ...props }) => <h4 {...props} />,
                          h5: ({ node, ...props }) => <h5 {...props} />,
                          h6: ({ node, ...props }) => <h6 {...props} />,
                          strong: ({ node, ...props }) => <strong {...props} />,
                          em: ({ node, ...props }) => <em {...props} />,
                          blockquote: ({ node, ...props }) => (
                            <blockquote {...props} />
                          ),
                        }}
                      >
                        {fixDocPaths(String(msg.content || ""))}
                      </ReactMarkdown>
                    ) : (
                      <span>{msg.content}</span>
                    )}
                  </div>
                  {msg.sources && msg.sources.length > 0 && (
                    <div className="message-sources">
                      <small>Sources:</small>
                      <ul>
                        {msg.sources.map((source, idx) => (
                          <li key={idx}>
                            <a
                              href={source.url}
                              target="_blank"
                              rel="noopener noreferrer"
                            >
                              {source.title}
                            </a>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
              ))
            )}
            {isLoading && (
              <div className="chat-message assistant-message">
                <div className="message-content">
                  <div className="typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          <div className="chat-input-area">
            <textarea
              ref={inputRef}
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Ask about the documentation..."
              rows="1"
              disabled={isLoading}
              className="chat-input"
            />
            <button
              onClick={sendMessage}
              disabled={isLoading || !inputValue.trim()}
              className="chat-send-btn"
            >
              {isLoading ? "Sending..." : "Send"}
            </button>
          </div>
        </div>
      ) : (
        <button className="chat-toggle-btn" onClick={toggleChat}>
          <span>🤖</span>
        </button>
      )}
    </div>
  );
};

export default ChatWidget;
