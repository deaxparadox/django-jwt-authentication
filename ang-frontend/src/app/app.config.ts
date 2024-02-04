import { ApplicationConfig, importProvidersFrom } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideClientHydration, withHttpTransferCacheOptions } from '@angular/platform-browser';
import { HttpClientJsonpModule, HttpClientModule, HttpClientXsrfModule, provideHttpClient, withFetch } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes), 
    provideClientHydration(
      // withHttpTransferCacheOptions({
      //   includePostRequests: true,
      // }),
    ),
    provideHttpClient(withFetch())  
  ]
};
