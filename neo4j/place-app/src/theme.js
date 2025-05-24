// src/theme.js
import { createTheme } from '@mui/material/styles';
import { blueGrey, amber } from '@mui/material/colors';

const theme = createTheme({
  palette: {
    primary: {
      main: blueGrey[700], // Dark grey-blue for primary actions
    },
    secondary: {
      main: amber[500], // Amber for accents
    },
    background: {
      default: blueGrey[50], // Light grey-blue for overall background
      paper: '#fff', // White for cards/containers
    },
    text: {
      primary: blueGrey[900],
      secondary: blueGrey[600],
    },
  },
  typography: {
    fontFamily: ['"Roboto"', 'sans-serif'].join(','),
    h4: {
      fontWeight: 700,
      marginBottom: '1rem',
    },
    h5: {
      fontWeight: 600,
      marginBottom: '0.5rem',
    },
    body1: {
      lineHeight: 1.6,
    },
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 8, // Slightly rounded buttons
        },
      },
    },
    MuiPaper: { // Style for Paper component (used for cards)
      styleOverrides: {
        root: {
          borderRadius: 12, // More rounded cards
          boxShadow: '0px 4px 20px rgba(0, 0, 0, 0.05)', // Subtle shadow
        },
      },
    },
    MuiTextField: { // Style for text fields
      styleOverrides: {
        root: {
          '& .MuiOutlinedInput-root': {
            borderRadius: 8,
          },
        },
      },
    },
  },
});

export default theme;