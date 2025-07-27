rule auto_rule_20250727024925_7423 {
  strings:
    $o0 = "off_40E520" wide ascii nocase
    $o1 = "UnwindUp1_0" wide ascii nocase
    $o2 = "byte_40E668" wide ascii nocase
  condition:
    3 of ($o*)
}