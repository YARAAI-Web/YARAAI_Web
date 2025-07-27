rule auto_rule_20250726200920_9365 {
  strings:
    $o0 = "dword_16D24" wide ascii nocase
    $o1 = "stru_16D00" wide ascii nocase
    $o2 = "KeInsertQueueApc" wide ascii nocase
    $o3 = "IoFreeMdl" wide ascii nocase
    $o4 = "x9004060" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726200924_6631 {
  strings:
    $o0 = "x9005094" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726200929_3910 {
  condition:
    auto_rule_20250726200920_9365 or auto_rule_20250726200924_6631
}