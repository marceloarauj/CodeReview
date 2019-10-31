Posts = new Mongo.Collection('posts');

Posts.publish = function(message, name) {
 var params = {
  message: message,
  time: new Date(),
  userId: Meteor.userId(),
  name: name
 };

 this.insert(params);
 winston.info("Posts.publish: ", params);
};

Posts.list = function(userIds) {
 return this.find(
  {userId: {$in: userIds}},
  {sort: {time: -1, name: 1}}
 );
};

winston = Meteor.npmRequire("winston");
winston.add(winston.transports.File, { 
 filename: "../application.log",
 maxsize: 1024
});

  
Accounts.onCreateUser(function(options, user) {
    if (user.services.facebook) {
     var facebook = user.services.facebook;
     user['profile'] = {
      name: facebook.name
     };
    } else {
     user['profile'] = options.profile;
    }
    return user;
   });

