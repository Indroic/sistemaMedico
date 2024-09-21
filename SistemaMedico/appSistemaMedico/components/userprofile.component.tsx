import React from "react";

import { Layout, Avatar, Text } from "@ui-kitten/components";
import { StyleSheet } from "react-native";

export default function UserProfile() {
  return (
    <Layout style={styles.container}>
      <Text>indroic</Text>
      <Avatar source={require("../assets/icon.png")} />
    </Layout>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    alignItems: "center",
    gap: 5,
    backgroundColor: "#00FF0000",
  },
});
