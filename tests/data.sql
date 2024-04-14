INSERT INTO user ( fullname, username,  email, password, terms_and_conditions)
VALUES 
    ('Test User', 'test', 'test@example.com', 'scrypt:32768:8:1$5k3OdH2FrjqOsls1$a6f9d3748749abe6926b6e3479a1dc1ae11f97873adb8091fdba84125dc5c065d86aef819d536e51f0f58fce53c7e4629aacce17dc97efd73c566526e8bc1a7e', 'True'),
    ('other', '', '', 'scrypt:32768:8:1$5k3OdH2FrjqOsls1$a6f9d3748749abe6926b6e3479a1dc1ae11f97873adb8091fdba84125dc5c065d86aef819d536e51f0f58fce53c7e4629aacce17dc97efd73c566526e8bc1a7f', 'True');