account = {
	"Username":"",
	"Password":""
}
license = "xxx"
tradeset = {
	"BaseTrade":"0.005",
	"C1":"40", 					#5-95
	"C2":"49", 					#5-95
	"NumberOfTrade":"3", 				#max limit 200
	"MultiplyOnWin":"1", 				## 0 untuk OFF 
	"MultiplyOnLose":"0.1", 				## 0 untuk OFF 
	"MaxBaseTrade":"0",				# 0 untuk OFF
	"ResetOnLoseMaxTrade":"ON", 			# ON/OFF
	"StopOnLoseMaxTrade":"ON",			# ON/OFF
	"TargetProfit":"50",				#0 untuk OFF
	"ClientSeed":"9999",				#max 32 digits
	"RecoveryMultiplier":"2.2",			# 1 untuk OFF
	"RecoveryIncrease":"0"	 			# 0 untuk OFF. Increase your BaseTrade If Lose
}

tools = {
	"AddDelayTrade":"0",				#Delay Per Trade
	"AddDelayTradeWin":"0",				#Delay Per Trade Win
	"AddDelayTradeLose":"0"				#Delay Per Trade Lose
}
