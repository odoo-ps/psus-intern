import JournalEntry from "./JournalEntry";

/**
 * a data interface contains currentText and journalList elements 
 */
 interface JournalData {
	currentText:string;
	journalList:JournalEntry[];
}

export default JournalData;