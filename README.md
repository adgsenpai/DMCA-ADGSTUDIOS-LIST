
# DMCA-ADGSTUDIOS-LIST

<img src="https://github.com/adgsenpai/DMCA-ADGSTUDIOS-LIST/assets/45560312/d9eb6380-4c09-4cb6-8c09-b363691e7984" width="250px">

## Overview
This repository hosts a list of URLs from the `adgstudios.co.za` domain that have been subject to DMCA takedown requests. The purpose of this repository is to maintain transparency and efficiency in handling DMCA requests and ensuring compliance.

## Fetching the DMCA List
To view the current list of DMCAed URLs, you can use the following `curl` command:
```bash
curl https://raw.githubusercontent.com/adgsenpai/DMCA-ADGSTUDIOS-LIST/main/static/db/list.txt
```

## Submitting a DMCA Takedown Request
If you wish to submit a DMCA takedown request for a page hosted under the `adgstudios.co.za` domain, please follow these steps:

1. **Fork the Repository**: Fork the `DMCA-ADGSTUDIOS-LIST` repository to your own GitHub account.

2. **Create a Pull Request**: Add the URL of the page you are requesting to be taken down to the `list.txt` file. Then, create a pull request to the original repository with your changes.

3. **Include Proof**: In your pull request, provide clear proof of the DMCA violation. This should include documentation proving ownership of the content or other legal justifications for the takedown request.

4. **Wait for Review**: Once submitted, your request will be reviewed. If the request is deemed valid, it will be approved and merged into the main list.

## Dynamic Content Management
Upon the approval and merging of a DMCA request, our content hosting environment will dynamically update to reflect these changes. This ensures immediate compliance with DMCA regulations.

## Future Work

### Integration with Lumen Database
We are currently exploring opportunities to enhance the efficiency and scope of our DMCA management process by integrating with the Lumen Database. Lumen Database, managed by the Berkman Klein Center for Internet & Society at Harvard University, provides a comprehensive and public database of DMCA notices and requests.

Our goal is to dynamically fetch data from the Lumen Database to keep our DMCA list up-to-date with the latest and most accurate information. However, this integration is contingent upon receiving an API key from Lumen Database. We are in the process of obtaining this key and hope to implement this feature in the near future.

### Automation with GitHub Actions
Once we have access to the Lumen Database API, we plan to automate the update process of the DMCA list. By leveraging GitHub Actions, our system will be able to automatically fetch new DMCA data from the Lumen Database on a daily basis and update the list accordingly.

This automation will not only streamline our process but also ensure that our list is constantly refreshed with the latest information, making our compliance with DMCA requests more efficient and reliable.

We believe that these advancements will significantly enhance the way we handle DMCA requests, making our response more proactive and data-driven.

## Contact
For any queries or further assistance, please reach out via [email link](mailto:adg@adgstudios.co.za).

## License
[MIT License](LICENSE)
