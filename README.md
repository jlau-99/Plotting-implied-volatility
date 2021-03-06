# Plotting-implied-volatility

Problem:
Use the CBOE webpage https://www.cboe.com/delayed_quotes/goog/quote_table to obtain current quotes for Call options on Alphabet (GOOG) expiring in January 2023, excluding all options with a log-moneyness below −0.2 or above 0.2. Compute the mid price (average of bid and ask prices) for these options. Using a risk-free rate of r = 0.01 and assuming no dividends, compute the implied volatility for each option (do not use the CBOE provided IVs), and plot this against the negative log-moneyness of the option. Do you observe a smile? A skew? (If working in excel, the ‘solver’ add-in may be useful to compute implied volatilities – if the solver has difficulty computing the implied volatilites for options far out of the money, then exclude them. You may find it easier to compute using Matlab, R or Python, if you are comfortable with one of these languages.)

The code and the csv file have to be in the same folder.
