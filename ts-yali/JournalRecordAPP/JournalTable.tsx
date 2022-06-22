import React from "react";
import "./App.css";
import JournalEntry from "./JournalEntry";

/**
 * a data interface delivers local props.
 */
interface JournalTableProps {
	journalList: JournalEntry[];
	toggleDoneJournalEntryHandler:(index:number)=>void;
	deleteJournalEntryHandler: (index: number) => void;   
}
/**
 * a class of JournalTable .
 */
class JournalTable extends React.Component<JournalTableProps> {
	/**
	 * constractor takes props as parameter 
	 */
	 constructor(journalTableProps: JournalTableProps) {
		super(journalTableProps);
		this.getJournalRow = this.getJournalRow.bind(this);
	}

	/**
	 * Render JSX Content.
	 * @returns JSX Element.
	 */
	render(): JSX.Element {
		let journalRows = this.props.journalList.map(this.getJournalRow);
		return (
			<table className="pure-table">
				<thead>
					<tr>
                        <th>Status</th>
						<th>Timestamp</th>
						<th>Entry</th>
                        <th>Action</th>
						<th>Action</th>
					</tr>
				</thead>
				<tbody>{journalRows}</tbody>
			</table>
		);
	}

	/**
	 * a method return the row 
	 * @param journalItem 
	 * @param index 
	 * @returns 
	 */
	private getJournalRow(journalItem: JournalEntry, index: number) {
		return (
			<tr key={journalItem.timeStamp.getSeconds()}>
                <td>{journalItem.status}</td>
				<td>
					{journalItem.timeStamp.toLocaleDateString()}{" "}
					{journalItem.timeStamp.toLocaleTimeString()}
				</td>
				<td>{journalItem.textEntry}</td>
                <td>
                    <button
                        className="pure-button"
                        onClick={this.props.toggleDoneJournalEntryHandler.bind(this, index)}
                    >    
                    Toggle
                    </button>
                </td>   
                
				<td>
					<button
						className="pure-button"
						onClick={this.props.deleteJournalEntryHandler.bind(this, index)}
					>
					Delete
					</button>
				</td>
			</tr>
		);
	}
}

export default JournalTable;