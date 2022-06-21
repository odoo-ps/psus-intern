/**
 * a data interface contains status, timeStamp, textEntry elments
 */
interface JournalEntry {
    status:string;
	timeStamp:Date;
	textEntry:string;
}

export default JournalEntry;