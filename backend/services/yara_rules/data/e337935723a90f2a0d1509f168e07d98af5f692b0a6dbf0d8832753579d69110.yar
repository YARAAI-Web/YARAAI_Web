rule auto_rule_20250727034458_6592 {
  strings:
    $o0 = "lpchText" wide ascii nocase
    $o1 = "wData" wide ascii nocase
    $o2 = "dwDesiredAccess" wide ascii nocase
    $o3 = "hTemplateFile" wide ascii nocase
    $o4 = "NotifyWinEvent" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250727034501_4668 {
  strings:
    $o0 = "wOemChar" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727034513_2085 {
  condition:
    auto_rule_20250727034458_6592 or auto_rule_20250727034501_4668
}