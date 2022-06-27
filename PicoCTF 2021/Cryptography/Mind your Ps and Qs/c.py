public static void main (String[] args) {

    BigInteger N,phiN,e,d,m,c;

    // chipertext c, plaintext m

    N = new BigInteger ("public static void main (String[] args) {

    BigInteger N,phiN,e,d,m,c;

    // chipertext c, plaintext m

    N = new BigInteger ("public static void main (String[] args) {

    BigInteger N,phiN,e,d,m,c;

    // chipertext c, plaintext m

    N = new BigInteger ("769457290801263793712740792519696786147248001937382943813345728685422050738403253");

    e = new BigInteger ("65537");

    c = new BigInteger ("8533139361076999596208540806559574687666062896040360148742851107661304651861689");

    phiN = new BigInteger ("21748096742659849357018698040199616792045282095099285468703513272637607311895366864257192785335233959058309060465868423951823285357297913125406449247738183679866482270532707596677244578324683864074431419149661562939376104607869781204868324933316666364155001553295827687037711471146642763970634674131635418276");

    d = e.modInverse(phiN);
    m = c.modPow(d, N);

    System.out.println("d = "+d);           
    System.out.println("m = "+m);

    System.out.println("m in base 256 = "+base256(m));
    System.out.println("Convert with ASCII \n"+ Encode256(base256(m)));

}

static ArrayList<BigInteger> base256 (BigInteger M) {
BigInteger base = new BigInteger("256");
    ArrayList<BigInteger> message256 = new ArrayList<BigInteger>();
BigInteger sisa=M;
BigInteger k;
double z = Double.parseDouble(M.toString());
double p = Math.floor(Math.log(z)/Math.log(256));
int r = (int) p;
    for (int j=0;j<=r;j++){
        k=sisa.mod(base);
        sisa=sisa.divide(base);
        message256.add(k);
}
return message256;
}

static String Encode256 (ArrayList<BigInteger> ascii) {
String ascii256="";
int g,dmp;
for (int i=0;i<ascii.size();i++) {
g = Integer.parseInt(""+ascii.get(i));
ascii256=ascii256+( (char) g );
}
return ascii256;
}");

    e = new BigInteger ("65537");

    c = new BigInteger ("5035028646289403967446356090900614024724984911944639699234793220898497706186123226210199790989613849953542047021633331398057077596600815193940830692730376382829474208609200046676663440957657102570794842099284679728898437831331557960967948540809799255902703014867201045003016001267189341232653910252303505881");

    phiN = new BigInteger ("21748096742659849357018698040199616792045282095099285468703513272637607311895366864257192785335233959058309060465868423951823285357297913125406449247738183679866482270532707596677244578324683864074431419149661562939376104607869781204868324933316666364155001553295827687037711471146642763970634674131635418276");

    d = e.modInverse(phiN);
    m = c.modPow(d, N);

    System.out.println("d = "+d);           
    System.out.println("m = "+m);

    System.out.println("m in base 256 = "+base256(m));
    System.out.println("Convert with ASCII \n"+ Encode256(base256(m)));

}

static ArrayList<BigInteger> base256 (BigInteger M) {
BigInteger base = new BigInteger("256");
    ArrayList<BigInteger> message256 = new ArrayList<BigInteger>();
BigInteger sisa=M;
BigInteger k;
double z = Double.parseDouble(M.toString());
double p = Math.floor(Math.log(z)/Math.log(256));
int r = (int) p;
    for (int j=0;j<=r;j++){
        k=sisa.mod(base);
        sisa=sisa.divide(base);
        message256.add(k);
}
return message256;
}

static String Encode256 (ArrayList<BigInteger> ascii) {
String ascii256="";
int g,dmp;
for (int i=0;i<ascii.size();i++) {
g = Integer.parseInt(""+ascii.get(i));
ascii256=ascii256+( (char) g );
}
return ascii256;
}Z");

    e = new BigInteger ("65537");

    c = new BigInteger ("");

    phiN = new BigInteger ("21748096742659849357018698040199616792045282095099285468703513272637607311895366864257192785335233959058309060465868423951823285357297913125406449247738183679866482270532707596677244578324683864074431419149661562939376104607869781204868324933316666364155001553295827687037711471146642763970634674131635418276");

    d = e.modInverse(phiN);
    m = c.modPow(d, N);

    System.out.println("d = "+d);           
    System.out.println("m = "+m);

    System.out.println("m in base 256 = "+base256(m));
    System.out.println("Convert with ASCII \n"+ Encode256(base256(m)));

}

static ArrayList<BigInteger> base256 (BigInteger M) {
BigInteger base = new BigInteger("256");
    ArrayList<BigInteger> message256 = new ArrayList<BigInteger>();
BigInteger sisa=M;
BigInteger k;
double z = Double.parseDouble(M.toString());
double p = Math.floor(Math.log(z)/Math.log(256));
int r = (int) p;
    for (int j=0;j<=r;j++){
        k=sisa.mod(base);
        sisa=sisa.divide(base);
        message256.add(k);
}
return message256;
}

static String Encode256 (ArrayList<BigInteger> ascii) {
String ascii256="";
int g,dmp;
for (int i=0;i<ascii.size();i++) {
g = Integer.parseInt(""+ascii.get(i));
ascii256=ascii256+( (char) g );
}
return ascii256;
}
