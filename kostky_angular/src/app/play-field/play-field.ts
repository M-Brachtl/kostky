import { Component } from '@angular/core';


@Component({
  selector: 'play-field',
  imports: [],
  templateUrl: './play-field.html',
  styleUrl: './play-field.css'
})
export class PlayField {
  dice = (): number[] => {
    let diceArray: number[] = [];
    for (let i = 0; i < 6; i++) {
      const randomNumber = Math.floor(Math.random() * 6) + 1;
      diceArray.push(randomNumber);
    }
    return diceArray;
  }
  
}
