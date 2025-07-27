rule auto_rule_20250727010126_4617 {
  strings:
    $o0 = "dword_427970" wide ascii nocase
    $o1 = "dword_4279A0" wide ascii nocase
    $o2 = "aGsyst12111cgcr" wide ascii nocase
  condition:
    3 of ($o*)
}