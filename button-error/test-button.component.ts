import { Component, EventEmitter, Output, OnInit } from '@angular/core';

@Component({
  selector: 'app-test-button',
  templateUrl: './test-button.component.html',
  styleUrls: ['./test-button.component.css']
})
export class TestButtonComponent implements OnInit {
  @Output()
  click: EventEmitter<MouseEvent>;

  constructor() {
    this.click = new EventEmitter<MouseEvent>();
  }

  clicked(e: MouseEvent) {
    this.click.emit(e);
  }

  ngOnInit() {}
}