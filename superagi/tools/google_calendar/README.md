<p align="center">
  <a href="https://superagi.com//#gh-light-mode-only">
    <img src="https://superagi.com/wp-content/uploads/2023/05/Logo-dark.svg" width="318px" alt="SuperAGI logo" />
  </a>
  <a href="https://superagi.com//#gh-dark-mode-only">
    <img src="https://superagi.com/wp-content/uploads/2023/05/Logo-light.svg" width="318px" alt="SuperAGI logo" />
  </a>
</p>

# SuperAGI - Google Calendar Toolkit

Introducing the Google Calendar Toolkit, a powerful integration for SuperAGI. With the Google Calendar toolkit, you have the ability to do the following:

1. **Create Calendar Events**
2. **List your Calendar Events**
3. **Fetch an event from your Calendar**
4. **Delete Calendar Events**

## ⚙️ Installation

### ⚒️ Setting up of SuperAGI

Set up SuperAGI by following the instructions given [here](https://github.com/TransformerOptimus/SuperAGI/blob/main/README.MD)

# ✅ Quickstart Guide:

In order to get started with integrating Google Calendar with SuperAGI, you need to do the following:

## API Creation and OAuth Consent Screen

1. Go to Google Developer Console:
[https://console.cloud.google.com/](https://console.cloud.google.com/) & Create a new project. If you’re having an existing project, you can proceed with that as well:

![GC1](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/9e4299c8-aa5e-49fd-b069-f07a50419e24)


2. After the project is created/you’re in your selected project, head to “APIs and Services”

![GC2](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/36462ef8-3f28-4c42-a32a-36b6f5489a25)


3. Click on “ENABLED APIS AND SERVICES” and search for “Google Calendar”

![GC3](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/792996f4-5f90-497f-a0d8-00556de3f3c3)
![GC4](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/4fd88f68-5401-4192-ae73-832d1165f532)


4. Enable the API
 
 ![GC5](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/f0b0ce29-2629-46da-93a9-9eeee518cbaf)
  
5. Once the API is Enabled, go to “OAuth Consent Screen” 

![GC6](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/8543411a-dc0c-417c-9197-09f9048c27b9)

6. Select your User Type as “External” and click on "Create"

![GC7](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/07e7da07-ccfb-417f-9bcd-83feb3d806af)

7. Fill in the required details such as the App Information, App Domain, Authorized Domain, and Developer contact information. Once filled in, click “Save and Continue” 

![GC8](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/224efa66-53a9-4161-8bf0-92db4e297d7a)

8. On the next page, you don’t need to select the scopes. Proceed to “save and continue” and at the final page, review the process and click “Back to Dashboard”.  With this, you’ve created your OAuth Consent Screen for Google Calendar.
   
9. You can go ahead and click the “Publish App” 

![GC9](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/6a3c6e5e-05f8-4482-9023-52effa7e09dd)

## 🔧 Configuring endpoints & obtaining Client ID and Client Secret Key

In order to obtain the Client ID and Secret ID, you need to do the following steps: 

1. Go to “Credentials” Page

![GC10](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/a42b885b-8b10-4af8-b690-afb17ac9581d)

2. Click on “Create Credentials” and click on “OAuth Client ID”

![GC11](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/86210cda-b4d1-49cc-a796-3c54bb2c80d9)

![GC12](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/11a568c1-a8b6-4fcc-8070-0006cfcb2494)

3. Once you click on OAuth Client ID, choose the type of application as “Web Application” and give it a name of your choice

![GC13](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/ca0e76a8-fa55-4648-92b5-55d309b3dc4f)

4. Create JavaScript Origins and add the following details as shown in the image: 

![GC14](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/b04d485a-0696-4207-95d8-e464ced6c300)

5. Go to Authorized redirect URIs and add the following as per the image: 

![GC15](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/169ed795-21da-4bf2-9b0c-fbd107be1e5c)

6. Once you’re completed with adding the Authorized redirect URIs, you can click “Create” to obtain the Client ID and Client Secret Key

![GC16](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/a8c9d126-4f6d-4a0e-b534-d06fbb45c162)

7. Copy the Client ID and Secret Key and save it in a file. 

## Configuring your Client ID, Secret Key and Authenticating Calendar with SuperAGI

Once the ClientID and Secret Key are obtained, you can configure and authorize Calendar to be used with SuperAGI by following these steps: 

1. Add your Client ID and Client Secret Key on the toolkit page and click on “Update Changes”

![GC_17](https://github.com/TransformerOptimus/SuperAGI/assets/133874957/bd38fbdc-f7f3-4baf-880d-52fac28834e9)

2. Click on “Authenticate Tool” - which will now take you to the OAuth Flow. 

Once the OAuth Authentication is complete, you can now start using SuperAGI Agents with Google Calendar!
