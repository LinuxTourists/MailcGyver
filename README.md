# MailcGyver

MailcGyver is a featureless KISS SMTP Server with integrated LDA for Maildir.


## SSL/TLS

MailcGyver is designed to use stunnel for transport encryption. 
Therefore port (2525) and host (127.0.0.1) are not configurable.

    # stunnel server configuration
    [stunnel.smtp]
    accept = public_ip_or_domain:587
    connect = 127.0.0.1:2525
    protocol = smtp

## Todo

  * decide known mailadress -> username handling
  * complete `IncommingThread()`
    * determine mailadress -> username -> Maildir location
  * implement `OutgoingThread()`
    * simple vise-versa to server (client implementation)
    * SMTP-Auth PLAIN 
  * Optional: Plugin based filtering
    * check for valid mail address format in "MAIL FROM"
    * grey listing?
    * spam detection?

  
 