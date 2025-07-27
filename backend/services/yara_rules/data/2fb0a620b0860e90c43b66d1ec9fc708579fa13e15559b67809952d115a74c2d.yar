rule auto_rule_20250727044514_4986 {
  strings:
    $o0 = "dword_43460B" wide ascii nocase
    $o1 = "x6321" wide ascii nocase
    $o2 = "off_414BD2" wide ascii nocase
    $o3 = "lpmii" wide ascii nocase
  condition:
    4 of ($o*)
}