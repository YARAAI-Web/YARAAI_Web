rule auto_rule_20250727031814_9732 {
  strings:
    $o0 = "x912C" wide ascii nocase
    $o1 = "dword_42967C" wide ascii nocase
    $o2 = "dword_429598" wide ascii nocase
    $o3 = "dword_429510" wide ascii nocase
    $o4 = "dword_429590" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727031817_6722 {
  strings:
    $o0 = "x7B6AB626" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727031822_4920 {
  condition:
    auto_rule_20250727031814_9732 or auto_rule_20250727031817_6722
}