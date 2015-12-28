import simplenlg.framework.*;
 import simplenlg.lexicon.*;
 import simplenlg.realiser.english.*;
 import simplenlg.phrasespec.*;
 import simplenlg.features.*;

public class Sentence{

  public static void main(String[] args) {
    SPhraseSpec p = nlgFactory.createClause();
    p.setSubject("Mary");
    p.setVerb("chase");
    p.setObject("the monkey");

    String output2 = realiser.realiseSentence(p); // Realiser created earlier.
    System.out.println(output2);

  }


}
