 $Begin = Get-Date -Date '11/16/22022 08:00:00'
$End = Get-Date -Date '11/17/2022 08:00:00'
Get-EventLog -LogName System -EntryType Error -After $Begin -Before $End
 
 Get-EventLog -LogName System -EntryType Error >C:\Users\sytyg\Desktop\error.txt
 
 Get-EventLog -LogName Application -Source Outlook | Where-Object {$_.EventID -eq 16} |
              Select-Object -Property Source, EventID, InstanceId, Message
              
Get-EventLog -LogName System -Newest 20

PS C:\WINDOWS\system32> $Events = Get-EventLog -LogName System -Newest 500
$Events | Group-Object -Property Source -NoElement | Sort-Object -Property Count -Descending

Count Name                     
----- ----                     
  125 Service Control Manager  
  113 Microsoft-Windows-Kern
   70 Microsoft-Windows-Kern
   52 Microsoft-Windows-Wind
   37 DCOM                     
   29 Microsoft-Windows-Time
   28 Server                   
   17 Microsoft-Windows-Powe
   15 Microsoft-Windows-Kern
    5 EventLog                 
    2 Microsoft-Windows-DNS-
    1 Microsoft-Windows-Ntfs   
    1 Win32k                   
    1 disk                     
    1 volsnap                  
    1 Schannel                 
    1 Microsoft-Windows-User
    1 Microsoft-Windows-WLAN
