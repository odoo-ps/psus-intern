import React from "react";
import "./App.css";

/**
 * a interface contains currentInPutText, textHandler function and addJournalHandler function
 * will delever the props
 */
 interface JournalEntryProps {
	currentText:string;
	textHandler:(event:React.FormEvent<HTMLInputElement>)=>void;
	addJournalHandler:()=>void;
}


/**
 * a class of JournalEntryPanel
 */
class JournalEntryPanel extends React.Component<JournalEntryProps> {

	/**
	 * Render JSX Content.
	 * @returns JSX Element.
	 */
	render(): JSX.Element {
		return (
			<div>
				<input
					className="pure-u-12-24"
					type="text"
					style={
						{	
						  width:300,
						  height:30
						}
					}
					value={this.props.currentText}
					
					onChange={this.props.textHandler}
					
				/>
				<p />
				<button
					className="pure-button pure-button-primary"
					onClick={this.props.addJournalHandler}
				>
					Add new Todo item
				</button>
			</div>
		);
	}
}

export default JournalEntryPanel;