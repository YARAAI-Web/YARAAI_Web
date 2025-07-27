rule auto_rule_20250727015453_6914 {
  strings:
    $o0 = "x3084588F8E36104FLL" wide ascii nocase
    $o1 = "qword_14113A2A0" wide ascii nocase
    $o2 = "x7FC61A496D8DF8FCLL" wide ascii nocase
  condition:
    3 of ($o*)
}