$(document).ready(function () {
  function nav() {
    $(".nav-toggle").click(function () {
      $(".nav").toggleClass("open");
    });
  }
  nav();
});

// function colorChanger() {
  
//   // color scheme selection (atleast 10) for every 5 seconds for now (supposed 5 mins)
//   const colorSchemeLight = [
//     ["#cccccc", "#abc", "#cccccc", "#cccccc", "#cccccc"],
//     ["#cccccc", "#cccccc", "#cccccc", "#cccccc", "#cccccc"],
//     ["#cccccc", "#cccccc", "#cccccc", "#cccccc", "#cccccc"],
//     ["#cccccc", "#cccccc", "#cccccc", "#cccccc", "#cccccc"],
//     ["#cccccc", "#cccccc", "#cccccc", "#cccccc", "#cccccc"],
//   ]

//   const colorSchemeDark = [
//     ["#cccccc", "#cccccc", "#cccccc", "#cccccc", "#cccccc"],
//     ["#cccccc", "#cccccc", "#cccccc", "#cccccc", "#cccccc"],
//     ["#cccccc", "#cccccc", "#cccccc", "#cccccc", "#cccccc"],
//     ["#cccccc", "#cccccc", "#cccccc", "#cccccc", "#cccccc"],
//     ["#cccccc", "#cccccc", "#cccccc", "#cccccc", "#cccccc"],
//   ]
  
//   // initialize color - light
//   const bgPrimaryLight = colorSchemeLight[0][0];
//   const bgSupportLight = colorSchemeLight[0][1];
//   const textPrimaryLight = colorSchemeLight[0][2];
//   const textSecondaryLight = colorSchemeLight[0][3];
//   const supportLight = colorSchemeLight[0][4];
  
//   // initialize color - dark
//   const bgPrimaryDark = colorSchemeLight[0][0];
//   const bgSupportDark = colorSchemeLight[0][0];
//   const textPrimaryDark = colorSchemeLight[0][0];
//   const textSecondaryDark = colorSchemeLight[0][0];
//   const supportDark = colorSchemeLight[0][0];
  
//   // color setter - light
//   document.documentElement.style.setProperty(
//     "--color-background-primary-light",
//     bgPrimaryLight
//   );

//   document.documentElement.style.setProperty(
//     "--color-background-support-light",
//     bgSupportLight
//   );
  
//   // color setter - dark
//   document.documentElement.style.setProperty(
//     "--color-background-primary-dark",
//     bgPrimaryDark
//   );
// }

// setInterval(colorChanger, 5000);

