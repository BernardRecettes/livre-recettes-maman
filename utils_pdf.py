from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime
import io

def generer_fiche_recette_pdf(rec, ing_recette, id_recette_str, image_path=None):
    """
    Génère un PDF de fiche recette avec titre, ingrédients, instructions, etc.
    
    Paramètres :
    - rec : DataFrame row avec titre, instructions, température, temps_cuisson, note, etc.
    - ing_recette : DataFrame filtré des ingrédients pour cette recette
    - id_recette_str : l'id_recette (ex: "P1-1")
    - image_path : chemin optionnel vers l'image manuscrite
    
    Retour : bytes du PDF
    """
    
    # Buffer en mémoire
    buffer = io.BytesIO()
    
    # Création du PDF
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=0.5*inch, leftMargin=0.5*inch,
                            topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    story = []
    styles = getSampleStyleSheet()
    
    # Style personnalisé pour le titre
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor("#4a2c2a"),
        spaceAfter=12,
        alignment=1  # center
    )
    
    # Titre
    titre = Paragraph(str(rec["titre"]), title_style)
    story.append(titre)
    
    # Info recette (origine, catégorie, température, temps)
    info_text = f"""
    <b>Origine :</b> {rec.get('origine', 'N/A')}<br/>
    <b>Catégorie :</b> {rec.get('id_categorie', 'N/A')}<br/>
    <b>Température :</b> {rec.get('temperature', 'N/A')} | <b>Temps de cuisson :</b> {rec.get('temps_cuisson', 'N/A')}
    """
    story.append(Paragraph(info_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Ingrédients
    story.append(Paragraph("<b>Ingrédients</b>", styles['Heading2']))
    for i, ligne in ing_recette.iterrows():
        ingredient = str(ligne["ingredients"])
        story.append(Paragraph(f"• {ingredient}", styles['Normal']))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Instructions
    story.append(Paragraph("<b>Instructions</b>", styles['Heading2']))
    instructions = str(rec.get("instructions", "")).replace("\n", "<br/>")
    story.append(Paragraph(instructions, styles['Normal']))
    
    # Note si présente
    if rec.get("note") and str(rec.get("note")).strip():
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("<b>Note</b>", styles['Heading2']))
        note = str(rec.get("note")).replace("\n", "<br/>")
        story.append(Paragraph(note, styles['Normal']))
    
    # Image manuscrite si disponible
    if image_path:
        story.append(PageBreak())
        story.append(Paragraph("<b>Recette originale manuscrite</b>", styles['Heading2']))
        try:
            img = Image(image_path, width=6*inch, height=8*inch)
            story.append(img)
        except:
            story.append(Paragraph("Image non disponible", styles['Normal']))
    
    # Pied de page (optionnel)
    story.append(Spacer(1, 0.3*inch))
    date_str = datetime.now().strftime("%d/%m/%Y")
    story.append(Paragraph(f"<i>Généré le {date_str}</i>", styles['Normal']))
    
    # Génération du PDF
    doc.build(story)
    buffer.seek(0)
    
    return buffer.getvalue()
