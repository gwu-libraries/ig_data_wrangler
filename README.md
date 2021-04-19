# ig_data_wrangler:  Instagram json-to-csv data wrangler

This program takes the json file generated by running [Instagram Scraper](https://github.com/arc298/instagram-scraper) as input, and generates an Excel file with one row per Instagram post.

## Data dictionary

| Column | Description |
| ------------- | ------------- |
| post_id | Instagram post ID |
| datetime | Instagram post date/time  |
| likes | Number of likes at time of scraping  |
| n_comments | Number of comments at time of scraping  |
| n_unique_commenters | Number of unique Instagram users who commented on the post, at time of scraping  |
| n_owner_comments | Number of comments on the post's comment thread that were from the post's owner, at time of scraping  |
| media_link | URL hyperlink to the live post |
| caption | post caption, at time of scraping |
