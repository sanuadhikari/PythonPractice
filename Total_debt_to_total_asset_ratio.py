Tl=float(input("enter the liability of company"))
TE=float(input("enter the equity of company"))
#debt_to_asset_ratio = TD/TA
#if TD/TA>1:
  #  print("total portion of debt is funded by asset")
#else:
  #  print("total portion of debt is funded by equity")
if Tl/TE > 2:
    print("safe to invest")
else:
    print("Not safe to invest")

