/**
 * Created by fgalvan on 18/10/16.
 */

var connection = new autobahn.Connection({
         url: 'ws://127.0.0.1:8081/ws',
         realm: 'realm1'
      });

connection.onopen = function (session, details) {

    console.log("connected!");

   // 1) subscribe to a topic
   function onevent(args) {
      console.log("Event:", args[0]);
   }

   // 2) publish an event
   session.publish('hackfunction', ['Hello, world!']);

/*   // 3) register a procedure for remoting
   function add2(args) {
      return args[0] + args[1];
   }
   session.register('com.myapp.add2', add2);

   // 4) call a remote procedure
   session.call('com.myapp.add2', [2, 3]).then(
      function (res) {
         console.log("Result:", res);
      }
   );*/
};

connection.onclose = function (reason, details) {
    console.log("Connection lost: " + reason)
};

connection.open();