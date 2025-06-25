# FFMPEG
> usado para converter PNG em video

```shell
ffmpeg -framerate 60 -start_number 0001 -i %04d.png -pix_fmt yuv420p out.mp4
```
