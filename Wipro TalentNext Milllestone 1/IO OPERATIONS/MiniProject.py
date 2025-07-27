''' 
Project: 1

Your friend has sent you a text file containing n lines. He sent a secret message 
with it, which tells you the place and time where you have to go and meet him. He 
challenges you to find it out without seeing the content of the file. He has given
hints to find it. Let’s surprise him by breaking the challenge with our python code.

Hints to find the secret message: 
1. The number of lines in the file tells you the meeting time.
Note: 1 <= number of lines <= 24. If the number of lines is exceeding 12, you need to 
convert it to 12 hour format. For example, 
* If the number of lines is 15, then the meeting time is 3 PM. 
* If the number of lines is 10, then the meeting time is 10 AM.
2. The word appearing for the maximum number of times tells you the meeting place.
Note: Meeting place will be a street name. For example,
* If the word Oxford appears for the maximum number of times, then meeting place is
Oxford Street.
* If the word Park appears for the maximum number of times, then meeting place is Park Street.

Sample input 1:
Cricket, a  bat-and-ball parkgame  played  between  two  teams  of  eleven park
players on a field at the parkcenter of which is a 20-metre (22-yard) pitch with a 
wicket at each end, each parkcomprising two bails balanced on three stumps. The 
batting parkscores runs by striking the ball bowled at the parkwicket with the 
parkbat, while the bowling and parkfielding side tries to prevent this and dismiss  
each parkplayer  (so  they  are  "out").  Means  of parkinclude  being bowled, 
when the ball hits the parkand dislodges the bails, and by the fielding side park
the ball after it is hit by the bat, but before it hits the park. When ten park
have been dismissed, the innings ends and the teams parkroles.

Sample output 1:
Meeting time: 9 AM
Meeting place: Park Street
Explanation: Number of lines is 9. The word park appears for the maximum of 15 times

Sample input 2:
Royal  Enfield  is  an  Indian Apollomotorcycle  manufacturing  
brand  with  tag  of "oldest Apollomotorcycle  brand  in  continuous  production"  
manufactured Apollofactories ChennaiApolloIndia. Licensed from Royal Enfield by indigenous 
Indian Madras Motors, it is now a Apollosubsidiary Eicher Motors Limited, an Indian 
Apolloautomaker. The company makes ApolloRoyal Enfield Bullet, and other  single-cylinder  
and  twin-cylinder Apollomotorcycles. First  produced Apollo in  1901,  Royal  Enfield is 
oldest  motorcycle Apollobrand  world  stillproduction, with Bullet model enjoying longest 
motorcycleApolloproduction run of all time. In 1990, Royal Enfield collaborated with Eicher 
ApolloGroup, an automotive company ApolloIndia, and merged with it 1994. Apart from bikes, 
Eicher ApolloGroup is involved in the production and sales Apollocommercial vehicles  and  
automotive  gears.  Although ApolloRoyal  Enfield  experienced difficulties 1990s,  and  
ceased Apollomotorcycle  production  at  their  Jaipur factory 2002, by 2013 Apollocompany 
opened a  new primary Apollofactory ApolloChennai  suburb  of  Oragadam  on strength  of  
increased  demand  for  its Apollomotorcycles. This was followed in Apollo2017 by inauguration 
another new  factory  of  a  similar  size  to facility  at ApolloOragadam  (capacity  600,000 
vehicles  per  year)  at  Vallam ApolloVagadal.  The  original  factory  at ApolloTiruvottiyur  
became  secondary,  and  continues  to  produce  some  limited-run motorcycle models

Sample output 2:
Meeting time: 8 PM
Meeting place: ApolloStreet
Explanation: Number of lines is 20 and converting it to 12 hour format we get 8 PM. 
The word Apollo appears for the maximum of 25 times
'''

def get_meeting_time(num_lines):
    if num_lines == 0:
        return "No lines in file."
    if num_lines <= 12:
        return f"{num_lines} AM"
    else:
        hour = num_lines - 12
        return f"{hour} PM"

def get_meeting_place(words):
    freq = {}
    for word in words:
        # Remove punctuation and keep only alphabetic characters
        cleaned = ''.join([c for c in word if c.isalpha()])
        if cleaned:
            freq[cleaned] = freq.get(cleaned, 0) + 1
    if not freq:
        return "No valid meeting place found.", "", 0  # Return 3 values always
    max_word = max(freq, key=freq.get)
    return f"{max_word} Street", max_word, freq[max_word]

def main():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        num_lines = len(lines)
        all_words = []
        for line in lines:
            all_words.extend(line.split())

        meeting_place, place_word, place_count = get_meeting_place(all_words)
        meeting_time = get_meeting_time(num_lines)

        print(f"\nMeeting time: {meeting_time}")
        print(f"Meeting place: {meeting_place}")

        print(f"\nExplanation:")
        print(f"Number of lines is {num_lines} and converting it to 12-hour format we get {meeting_time}.")
        if place_word:
            print(f"The word '{place_word}' appears for the maximum of {place_count} times.")
        else:
            print("No valid word found for meeting place.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
