rule auto_rule_20250726093546_1527 {
  strings:
    $o0 = "_cinit" wide ascii nocase
    $o1 = "x4020D4" wide ascii nocase
    $o2 = "doexit" wide ascii nocase
    $o3 = "byte_44A181" wide ascii nocase
    $o4 = "dword_40B004" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726093549_7075 {
  strings:
    $o0 = "dword_44A06C" wide ascii nocase
    $o1 = "old_esp" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726093554_9125 {
  condition:
    auto_rule_20250726093546_1527 or auto_rule_20250726093549_7075
}