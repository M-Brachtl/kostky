import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PlayField } from './play-field/play-field';


@Component({
  selector: 'app-root',
  imports: [RouterOutlet, PlayField],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected title = 'Kostky';

  // Point variables
  pointNow = 0;
  pointRound = 0;
  pointTotal = 0;

  // Counting point of chosen dice
  
}
