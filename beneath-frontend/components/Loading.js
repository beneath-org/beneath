import CircularProgress from "@material-ui/core/CircularProgress";
import Grid from "@material-ui/core/Grid";

const Loading = (props) => (
  <Grid container justify={props.justify}>
    <Grid item>
      <CircularProgress size={props.size} />
    </Grid>
  </Grid>
);

export default Loading;
