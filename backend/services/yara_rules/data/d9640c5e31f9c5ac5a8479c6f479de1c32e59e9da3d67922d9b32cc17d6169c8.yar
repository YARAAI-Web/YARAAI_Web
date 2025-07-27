rule auto_rule_20250726102355_1335 {
  strings:
    $o0 = "ModemStat" wide ascii nocase
    $o1 = "dword_434419" wide ascii nocase
    $o2 = "x8A3E" wide ascii nocase
    $o3 = "SrcHeight" wide ascii nocase
    $o4 = "dword_432704" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726102358_9547 {
  strings:
    $o0 = "SelectPalette" wide ascii nocase
    $o1 = "off_4162AC" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726102402_4339 {
  condition:
    auto_rule_20250726102355_1335 or auto_rule_20250726102358_9547
}