import 'dart:async';
import 'package:meta/meta.dart';

import 'package:last/dao/dao.dart';
import 'package:last/models/user_model.dart';
import 'package:last/models/api_models.dart';
import 'package:last/api_connection/api_connection.dart';

class UserRepository {
  final userDao = UserDao();

  Future<User> signInWithCredentials({
    required String username,
    required String password,
  }) async {
    UserLogin userLogin = UserLogin(username: username, password: password);
    Token token = await getToken(userLogin);
    User user = User(
      id: 0,
      username: username,
      token: token.token,
    );

    print("HELLO FROM API ${username} ${password}");

    await userDao.createUser(user);
    return user;
  }

  // Future<void> signUp(
  //     {required String userName,
  //     required String firstName,
  //     required String lastName,
  //     required String email,
  //     required String password,
  //     required String streetAddress,
  //     required String locality,
  //     required String city,
  //     required String state,
  //     required int pinCode}) async {
  //   UserDetails userDetails = UserDetails(
  //       username: userName,
  //       firstName: firstName,
  //       lastName: lastName,
  //       email: email,
  //       password: password);

  //   Address address = Address(
  //       streetAddress: streetAddress,
  //       locality: locality,
  //       city: city,
  //       state: state,
  //       pinCode: pinCode);

  //   UserSignup userSignup = UserSignup(user: userDetails, address: address);

  //   UserLogin registeredUser = await registerUser(userSignup);
  //   Token registeredUserToken = await getToken(registeredUser);
  //   User user = User(
  //     id: 0,
  //     username: userName,
  //     token: registeredUserToken.token,
  //   );
  //   await userDao.createUser(user);
  // }

  // Future<void> deleteToken({@required int id}) async {
  //   await userDao.deleteUser(id);
  // }

  // Future<void> signOut() async {
  //   print("Logging out");
  //   await deleteToken(id: 0);
  // }

  // Future<bool> hasToken() async {
  //   bool result = await userDao.checkUser(0);
  //   return result;
  // }

  // Future<bool> isSignedIn() async {
  //   return hasToken();
  // }

  Future<String> getUser() async {
    User user = await userDao.getUserById(0);
    return user.username;
  }
}
