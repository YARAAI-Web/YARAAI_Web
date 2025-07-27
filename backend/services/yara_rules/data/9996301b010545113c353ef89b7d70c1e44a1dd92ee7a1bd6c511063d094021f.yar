rule auto_rule_20250726112128_9139 {
  strings:
    $o0 = "CRecordset" wide ascii nocase
    $o1 = "GetInterfaceHook" wide ascii nocase
    $o2 = "SetRowsetCurrencyStatus" wide ascii nocase
  condition:
    3 of ($o*)
}