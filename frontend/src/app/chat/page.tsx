"use client";

import { useRef, useState, type FormEvent, type KeyboardEvent } from "react";
import {
  BookOpen,
  FileText,
  GraduationCap,
  LoaderCircle,
  MessageSquare,
  Plus,
  Send,
  Sparkles,
  UploadCloud,
} from "lucide-react";

type Source = {
  document_id?: string | null;
  filename: string;
  heading?: string | null;
  chunk_id?: number | null;
};

type Message = {
  role: "user" | "assistant";
  content: string;
  sources?: Source[];
};

const API_BASE = (process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000").replace(/\/$/, "");

const suggestions = [
  "Explain the key concepts in my notes",
  "Summarise the most important points",
  "Create a revision plan from my material",
];

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [question, setQuestion] = useState("");
  const [busy, setBusy] = useState(false);
  const [uploading, setUploading] = useState(false);
  const [documents, setDocuments] = useState<string[]>([]);
  const [notice, setNotice] = useState("");
  const fileInput = useRef<HTMLInputElement>(null);

  async function uploadFile(file?: File) {
    if (!file) return;
    if (file.type !== "application/pdf" && !file.name.toLowerCase().endsWith(".pdf")) {
      setNotice("Please choose a PDF file.");
      return;
    }

    if (file.size > 25 * 1024 * 1024) {
      setNotice("PDFs must be 25 MB or smaller.");
      return;
    }

    setUploading(true);
    setNotice("");
    const body = new FormData();
    body.append("file", file);

    try {
      const response = await fetch(`${API_BASE}/documents/upload`, { method: "POST", body });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "Upload failed. Please try again.");
      setDocuments((current) => [...current, data.filename || file.name]);
      setNotice(`Added ${data.filename || file.name} to your study library.`);
    } catch (error) {
      setNotice(error instanceof Error ? error.message : "Could not connect to VidyAI. Check the backend URL.");
    } finally {
      setUploading(false);
      if (fileInput.current) fileInput.current.value = "";
    }
  }

  async function sendMessage(event?: FormEvent) {
    event?.preventDefault();
    const text = question.trim();
    if (!text || busy) return;

    setMessages((current) => [...current, { role: "user", content: text }]);
    setQuestion("");
    setBusy(true);
    setNotice("");

    try {
      const response = await fetch(`${API_BASE}/rag/query`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: text }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "The question could not be answered.");
      setMessages((current) => [...current, {
        role: "assistant",
        content: data.answer || "I couldn't generate an answer. Please try again.",
        sources: data.sources || [],
      }]);
    } catch (error) {
      setMessages((current) => [...current, {
        role: "assistant",
        content: error instanceof Error ? error.message : "Could not connect to VidyAI. Check that the backend is running.",
      }]);
    } finally {
      setBusy(false);
    }
  }

  function onComposerKeyDown(event: KeyboardEvent<HTMLTextAreaElement>) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      void sendMessage();
    }
  }

  return (
    <main className="flex min-h-screen bg-[#f8f8f5] text-[#20211e]">
      <aside className="hidden w-[264px] shrink-0 flex-col border-r border-black/5 bg-white px-5 py-6 md:flex">
        <a href="/" className="mb-10 flex items-center gap-3 text-xl font-semibold tracking-tight">
          <span className="flex size-9 items-center justify-center rounded-xl bg-[#242820] text-white"><GraduationCap size={20} /></span>
          VidyAI
        </a>
        <button className="flex items-center gap-2 rounded-xl bg-[#25291f] px-4 py-3 text-sm font-medium text-white transition hover:bg-[#3b4033]" onClick={() => { setMessages([]); setNotice(""); }}>
          <Plus size={17} /> New conversation
        </button>
        <div className="mt-9">
          <p className="mb-3 px-2 text-[11px] font-semibold uppercase tracking-[0.16em] text-[#92958b]">Your workspace</p>
          <div className="flex items-center gap-3 rounded-xl bg-[#f4f5f0] px-3 py-3 text-sm font-medium">
            <MessageSquare size={17} className="text-[#68715c]" /> Academic chat
          </div>
        </div>
        <div className="mt-9 min-h-0 flex-1">
          <div className="mb-3 flex items-center justify-between px-2">
            <p className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#92958b]">Study library</p>
            <button aria-label="Upload a PDF" onClick={() => fileInput.current?.click()} className="rounded-lg p-1.5 text-[#777d70] hover:bg-[#f1f2ed]"><Plus size={16} /></button>
          </div>
          {documents.length === 0 ? (
            <p className="px-2 text-xs leading-5 text-[#9a9d94]">Your uploaded PDFs will appear here.</p>
          ) : (
            <ul className="space-y-1">{documents.map((name, index) => <li key={`${name}-${index}`} className="flex items-center gap-2 rounded-lg px-2 py-2 text-xs text-[#64695f]"><FileText size={15} className="shrink-0" /><span className="truncate">{name}</span></li>)}</ul>
          )}
        </div>
        <div className="rounded-xl bg-[#f6f7f2] p-3 text-xs leading-5 text-[#777d70]">
          <div className="mb-1 flex items-center gap-2 font-semibold text-[#454b3e]"><Sparkles size={14} /> Built for learning</div>
          Answers are grounded in the documents you upload.
        </div>
      </aside>

      <section className="flex min-h-screen min-w-0 flex-1 flex-col">
        <header className="flex h-[72px] items-center justify-between border-b border-black/5 bg-white/80 px-5 backdrop-blur md:px-9">
          <div className="flex items-center gap-3">
            <a href="/" className="font-semibold tracking-tight md:hidden">VidyAI</a>
            <span className="hidden h-5 w-px bg-black/10 md:block" />
            <div><p className="text-sm font-semibold">Academic assistant</p><p className="text-[11px] text-[#92958b]">Your personal study companion</p></div>
          </div>
          <button onClick={() => fileInput.current?.click()} disabled={uploading} className="inline-flex items-center gap-2 rounded-full border border-[#e4e6dd] bg-white px-3.5 py-2 text-xs font-medium text-[#4c5345] transition hover:bg-[#f4f5f0] disabled:opacity-60">
            {uploading ? <LoaderCircle size={15} className="animate-spin" /> : <UploadCloud size={15} />} <span className="hidden sm:inline">Upload PDF</span><span className="sm:hidden">Upload</span>
          </button>
          <input ref={fileInput} type="file" accept="application/pdf,.pdf" className="hidden" onChange={(event) => void uploadFile(event.target.files?.[0])} />
        </header>

        <div className="mx-auto flex w-full max-w-4xl flex-1 flex-col px-4 pb-6 pt-8 sm:px-8">
          {messages.length === 0 ? (
            <div className="flex flex-1 flex-col justify-center pb-12">
              <div className="mb-6 flex size-12 items-center justify-center rounded-2xl bg-[#e8eddc] text-[#59634c]"><BookOpen size={23} /></div>
              <p className="mb-3 text-xs font-semibold uppercase tracking-[0.18em] text-[#879078]">Learn with clarity</p>
              <h1 className="max-w-2xl text-3xl font-semibold leading-tight tracking-[-0.04em] sm:text-5xl">Your study material.<br /><span className="text-[#89927d]">A smarter way to understand it.</span></h1>
              <p className="mt-5 max-w-lg text-sm leading-6 text-[#777d70]">Upload your class notes, textbooks, or lecture PDFs. Ask questions and get explanations grounded in your own material.</p>
              <div className="mt-9 grid gap-3 sm:grid-cols-3">
                {suggestions.map((item) => <button key={item} onClick={() => setQuestion(item)} className="rounded-2xl border border-[#e8e9e2] bg-white p-4 text-left text-sm leading-5 text-[#555c4d] transition hover:-translate-y-0.5 hover:border-[#cbd2bd] hover:shadow-sm">{item}<span className="mt-4 block text-[#a0a596]">↗</span></button>)}
              </div>
              <button onClick={() => fileInput.current?.click()} className="mt-7 flex w-full max-w-md items-center gap-4 rounded-2xl border border-dashed border-[#cbd1c1] bg-white/70 p-4 text-left transition hover:bg-white">
                <span className="flex size-10 items-center justify-center rounded-xl bg-[#edf0e6] text-[#68735a]"><UploadCloud size={19} /></span>
                <span><span className="block text-sm font-semibold">Start by uploading a PDF</span><span className="mt-1 block text-xs text-[#92978b]">Your document becomes searchable study context</span></span>
              </button>
            </div>
          ) : (
            <div className="flex-1 space-y-7 pb-8">
              {messages.map((message, index) => (
                <article key={index} className={`flex gap-3 ${message.role === "user" ? "justify-end" : "justify-start"}`}>
                  {message.role === "assistant" && <span className="mt-1 flex size-8 shrink-0 items-center justify-center rounded-xl bg-[#e8eddc] text-[#59634c]"><Sparkles size={16} /></span>}
                  <div className={`max-w-[85%] rounded-2xl px-4 py-3.5 text-sm leading-7 ${message.role === "user" ? "bg-[#25291f] text-white" : "border border-[#e9eae4] bg-white text-[#454a40]"}`}>
                    <p className="whitespace-pre-wrap">{message.content}</p>
                    {!!message.sources?.length && <div className="mt-4 border-t border-black/5 pt-3"><p className="mb-2 text-[10px] font-semibold uppercase tracking-[0.14em] text-[#92978b]">Sources from your library</p><div className="flex flex-wrap gap-2">{message.sources.map((source, sourceIndex) => <span key={`${source.document_id}-${source.chunk_id}-${sourceIndex}`} className="inline-flex max-w-full items-center gap-1.5 rounded-lg bg-[#f4f5f0] px-2.5 py-1.5 text-[11px] text-[#626a57]"><FileText size={12} /><span className="truncate">{source.filename}{source.heading ? ` · ${source.heading}` : ""}</span></span>)}</div></div>}
                  </div>
                </article>
              ))}
              {busy && <div className="flex items-center gap-3 text-sm text-[#858b7b]"><LoaderCircle size={17} className="animate-spin" /> VidyAI is thinking through your material…</div>}
            </div>
          )}
          {notice && <p role="status" className="mb-3 rounded-xl bg-[#eef1e8] px-4 py-2.5 text-xs text-[#58634c]">{notice}</p>}
          <form onSubmit={sendMessage} className="sticky bottom-4 rounded-2xl border border-[#e2e4db] bg-white p-2 shadow-[0_12px_40px_rgba(30,35,20,0.08)]">
            <textarea value={question} onChange={(event) => setQuestion(event.target.value)} onKeyDown={onComposerKeyDown} rows={2} placeholder="Ask anything about your study material…" className="max-h-36 min-h-14 w-full resize-y bg-transparent px-3 py-2 text-sm leading-6 outline-none placeholder:text-[#a0a497]" />
            <div className="flex items-center justify-between px-1 pb-1">
              <button type="button" onClick={() => fileInput.current?.click()} className="inline-flex items-center gap-1.5 rounded-lg px-2 py-1.5 text-xs text-[#7b8271] hover:bg-[#f4f5f0]"><Plus size={14} /> Add PDF</button>
              <button type="submit" disabled={!question.trim() || busy} className="inline-flex items-center gap-2 rounded-xl bg-[#25291f] px-4 py-2 text-xs font-medium text-white transition hover:bg-[#3b4033] disabled:cursor-not-allowed disabled:opacity-40">Ask VidyAI <Send size={13} /></button>
            </div>
          </form>
          <p className="mt-3 text-center text-[10px] text-[#a1a497]">VidyAI can make mistakes. Check important information against your source material.</p>
        </div>
      </section>
    </main>
  );
}
