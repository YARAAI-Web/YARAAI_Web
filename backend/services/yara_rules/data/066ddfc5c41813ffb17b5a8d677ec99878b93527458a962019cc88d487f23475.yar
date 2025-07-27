rule auto_rule_20250727012742_9677 {
  strings:
    $o0 = "lpKids" wide ascii nocase
    $o1 = "DdeDisconnect" wide ascii nocase
    $o2 = "FindAtomW" wide ascii nocase
    $o3 = "SetSystemTimeAdjustment" wide ascii nocase
    $o4 = "fSearchOp" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727012745_6156 {
  strings:
    $o0 = "hNamedPipe" wide ascii nocase
    $o1 = "SetConsoleTitleW" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727012751_9512 {
  condition:
    auto_rule_20250727012742_9677 or auto_rule_20250727012745_6156
}