rule auto_rule_20250727015648_2610 {
  strings:
    $o0 = "TargetIp" wide ascii nocase
    $o1 = "fill_with_EOS_dwords" wide ascii nocase
    $o2 = "_IsZeroMan" wide ascii nocase
    $o3 = "dword_455E4C" wide ascii nocase
    $o4 = "dword_4570D0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727015651_4468 {
  strings:
    $o0 = "off_455CE8" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727015656_3114 {
  condition:
    auto_rule_20250727015648_2610 or auto_rule_20250727015651_4468
}