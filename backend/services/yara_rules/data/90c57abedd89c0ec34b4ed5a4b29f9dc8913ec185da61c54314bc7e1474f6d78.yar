rule auto_rule_20250726065036_5464 {
  strings:
    $o0 = "lpMessageCount" wide ascii nocase
    $o1 = "hWndInsertAfter" wide ascii nocase
    $o2 = "IsZoomed" wide ascii nocase
    $o3 = "PurgeComm" wide ascii nocase
    $o4 = "InterlockedExchangeAdd" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726065039_2143 {
  strings:
    $o0 = "uIDNewItem" wide ascii nocase
    $o1 = "byte_4438B7" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726065043_8928 {
  condition:
    auto_rule_20250726065036_5464 or auto_rule_20250726065039_2143
}