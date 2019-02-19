import { BrowserModule } from '@angular/platform-browser';
import { NgModule, ErrorHandler, Injectable } from '@angular/core';
import { FormsModule } from '@angular/forms';

import * as Sentry from "@sentry/browser";

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TestButtonComponent } from './test-button.component';

Sentry.init({
  dsn: "https://2fa804a1648046f5b52fdbed75ed8a18@sentry.io/1395265"
});

@Injectable()
export class SentryErrorHandler implements ErrorHandler {
  constructor() {}
  handleError(error) {
    Sentry.captureException(error.originalError || error);
    throw error;
  }
}

@NgModule({
  declarations: [AppComponent, TestButtonComponent],
  imports: [BrowserModule, AppRoutingModule],
  providers: [{ provide: ErrorHandler, useClass: SentryErrorHandler }],
  bootstrap: [AppComponent]
})

export class AppModule { }
