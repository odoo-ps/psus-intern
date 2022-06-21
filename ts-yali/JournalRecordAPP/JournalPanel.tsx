import "./App.css";
import JournalTable from "./JournalTable";
import JournalData from "./JournalData";
import JournalEntry from "./JournalEntry";
import JournalEntryPanel from "./JournalEntryPanel";
import React from "react";

/**
 * a class of JournalPanel 
 */
class JournalPanel extends React.Component<{}, JournalData> {
	/**
	 * a constructor takes {} as parameter and initialize Log State.
	 */
	constructor(props: {}) {
		super(props);
		this.state = {
			currentText:"",
			journalList:[],
		};
		this.textInputEventHandler = this.textInputEventHandler.bind(this);
		this.addJournalEventHandler = this.addJournalEventHandler.bind(this);
		this.toggleDoneJournalEntryEventHandler=this.toggleDoneJournalEntryEventHandler.bind(this);
		this.deleteJournalEntryEventHandler = this.deleteJournalEntryEventHandler.bind(this);   
	}
	/**
	 * Render JSX Content.
	 * @returns JSX Element.
	 */
	render(): JSX.Element {
		return (
			<div>
				<h1 className="post-title">Super Todo!</h1>
				<div>
					<JournalEntryPanel 
						currentText={this.state.currentText}
						textHandler={this.textInputEventHandler}
						addJournalHandler={this.addJournalEventHandler}
					/>
				</div>
				<p/>
				<div className="pure-u-1-2">
					<JournalTable 
						journalList={this.state.journalList}
						toggleDoneJournalEntryHandler={this.toggleDoneJournalEntryEventHandler}
						deleteJournalEntryHandler = {this.deleteJournalEntryEventHandler} 
                    />
				</div>
			</div>
		);
	}
    /**
	 * a method to prompt user input text to the textfeild 
	 * @param event 
	 */
	private textInputEventHandler(event: React.FormEvent<HTMLInputElement>) {
		let newTextValue = event.currentTarget.value;
		console.log("Got Text Change:  " + newTextValue);
		let journalList = this.state.journalList;
		this.setState({
			currentText: newTextValue,
			journalList: journalList,
		});
	}

	/**
	 * a method to add the list when user clicks the add button.
	 */
	private addJournalEventHandler() {
		let journalList = this.state.journalList;
		if (this.state.currentText) {
			let currentTime = new Date();
			let newEntry:JournalEntry = {
                status:"Pending",
				timeStamp:currentTime,
				textEntry:this.state.currentText,
			};
			journalList.push(newEntry);
			this.setState({
				currentText: "",
				journalList: journalList,
			});
		}
	}
	/**
	 * a method to change the status when user clicks the toggle button.
	 * @param index 
	 */
	private toggleDoneJournalEntryEventHandler(index:number){
     
		let journalList=this.state.journalList;
		if(journalList[index].status==="Pending"){   
		    journalList[index].status="Done";
		}
		else{
		    journalList[index].status="Pending"
		}
		
		
		this.setState({
		  currentText: this.state.currentText,
		  journalList: journalList,
		})
		
	  }
	/**
	 * a method to delete the list from journal when user clicks the delete button
	 * @param index 
	 */
	private deleteJournalEntryEventHandler(index:number) {
		console.log("Deleting Journal Entry:  " + index);
		let journalList = this.state.journalList;
		journalList.splice(index, 1);
		this.setState({
			currentText: this.state.currentText,
			journalList: journalList,
		});
	}
    
}

export default JournalPanel;