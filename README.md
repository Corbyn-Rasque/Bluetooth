# Bluetooth & Embedded Experimentation

The purpose of this repository is mainly to play around with and gain experience with bluetooth and its protocols. I've wanted to create HomeKit devices out of my Dyson Solarcycle desk lamp and Fellow Stagg EKG+ kettle for some time to allow for automation, and to my knowledge no one has taken on such a project yet.

The end target of this experimentation is to create something that can run on an ESP32-C6 and interface with HomeSpan for the HomeKit side of things. The python code is to accelerate experimentation with bluetooth protocols, without the overhead of managing state machines and concurrency on an embedded device. Python should help make the protocols more obvious to implement in C++ down the line (especially for encrypted handshakes, like with the Dyson lamp).

If you'd like to experiment or join the project, you are more than welcome to! 

# Dyson

For the Dyson, you will need to find your GUID and LTK for the encrypted handshake.

The project in its current state is able to successfully make a handshake with the lamp and send commands. State updating is still in progress. The handshake crypto itself can be found in ./dyson/bluetooth/authentication. Message structure can be found in ./dyson/lighting/solarcycle/messages.

There are two different kinds of handshakes: authentication and reauthentication. The former is only every used once to set up your lamp for the first time. Every other time, reauthentication can be used. The latter is implemented here; the former is unknown.