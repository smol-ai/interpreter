// import AssistantIcon from '@mui/icons-material/Assistant';

import { useState } from "react";
import "./Sidebar.css";

export default function Sidebar(props: {
  models: Array<{ name: string; displayName: string }>;
  selectedModel: string;
  onSelectModel: any;
  setOpenAIKey: any;
  openAIKey: string;
}) {
  const handleOpenAIButtonClick = () => {
    const key = prompt("Please enter your OpenAI key", props.openAIKey);
    if (key != null) {
      props.setOpenAIKey(key);
    }
  };
  const [reveal, setReveal] = useState(true);
  return (
    <>
      <div className={reveal ? "sidebar" : 'smolbar'}>
        <div className="logo">
          <button onClick={() => setReveal(!reveal)}>🐣</button> {reveal && "Smol Talk!"}
        </div>
        {reveal && (
        <div className="settings">
            <label className="header">Settings</label>
            <label>Model</label>
            <select
            value={props.selectedModel}
            onChange={(event) => props.onSelectModel(event.target.value)}
            >
            {props.models.map((model, index) => {
                return (
                <option key={index} value={model.name}>
                    {model.displayName}
                </option>
                );
            })}
            </select>
            <label>Credentials</label>
            <button className="button" onClick={handleOpenAIButtonClick}>Set OpenAI key</button>
        </div>
        )}
      </div>
    </>
  );
}
