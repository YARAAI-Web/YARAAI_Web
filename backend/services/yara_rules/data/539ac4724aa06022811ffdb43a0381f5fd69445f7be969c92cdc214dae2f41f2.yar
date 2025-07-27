rule auto_rule_20250726183725_5688 {
  strings:
    $o0 = "dword_44A3A4" wide ascii nocase
    $o1 = "_setenvp" wide ascii nocase
    $o2 = "dword_40B018" wide ascii nocase
    $o3 = "GetStringTypeW" wide ascii nocase
  condition:
    4 of ($o*)
}