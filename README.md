<b>Problem</b> : To create a reminder system for a transport company.<br>
<b>Features</b> :<br>
1. To generate notification before 7,15,30 days of Expiry.
            
<pre>Solution: A table has been created in the database named notification and using datetime api the differnce between the expiry date and the current date is calculated and a notification is generated with restrictions on duplicacy.</pre>

2.Mark as read Functionality :

<pre>Solution: A "is_read" boolean filed is added to the Notification table and a view is attached to the "Mark as read" button in the bell icon dropdown on the navigation bar which sets the "is_read" field to true and changes the notifications accordingly.</pre>
