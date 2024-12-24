import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';

export default function Copyright(props) {
  return (
    <Typography
      component="div"
      variant="body2"
      color="text.secondary"
      align="center"
      {...props}
    >
      <p style={{ marginBottom: '1px' }}>Powered by:</p>
      <Link
        style={{ marginRight: '4px' }}
        color="inherit"
        target="_blank"
        href="https://cartesi"
      >
        www.cartesi.io
      </Link>
      <Link
        style={{ marginRight: '4px' }}
        color="inherit"
        target="_blank"
        href="https://unicef.org"
      >
        www.unicef.org
      </Link>

      <span>{new Date().getFullYear()}</span>
    </Typography>
  );
}
