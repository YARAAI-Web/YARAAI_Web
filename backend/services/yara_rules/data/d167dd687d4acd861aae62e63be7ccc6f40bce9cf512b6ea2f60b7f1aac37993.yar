rule auto_rule_20250726161045_9849 {
  strings:
    $o0 = "off_42A592" wide ascii nocase
    $o1 = "dword_42B1EA" wide ascii nocase
    $o2 = "dword_42A552" wide ascii nocase
    $o3 = "x4E48" wide ascii nocase
    $o4 = "off_42A2EA" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726161049_0138 {
  strings:
    $o0 = "x7440u" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726161054_7651 {
  condition:
    auto_rule_20250726161045_9849 or auto_rule_20250726161049_0138
}