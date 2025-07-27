rule auto_rule_20250726084108_9042 {
  strings:
    $o0 = "UnwindUp6_0" wide ascii nocase
    $o1 = "GetStringTypeA" wide ascii nocase
    $o2 = "off_44BCA4" wide ascii nocase
    $o3 = "hard" wide ascii nocase
    $o4 = "tionAndSpinCount" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726084111_8903 {
  strings:
    $o0 = "_mtdeletelocks" wide ascii nocase
    $o1 = "_msize" wide ascii nocase
    $o2 = "terminated" wide ascii nocase
    $o3 = "byte_44BE9C" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726084119_3733 {
  condition:
    auto_rule_20250726084108_9042 or auto_rule_20250726084111_8903
}